import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getImageById, imageByLabel } from "../../redux/image";
import { getLabelsForExplore } from "../../redux/label";
import "./ExplorePage.css";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";
import { getSearchLabel } from "../../redux/searchLabel";

function ExplorePage() {
	
	// For organizing the loaded images
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	useEffect(() => {
		function handleColNum() {
			setColNum(parseInt((window.innerWidth - 40) / 340));
		}
		window.addEventListener("resize", handleColNum);
		return () => window.removeEventListener("resize", handleColNum);
	}, []);

	// Creating dispatch 
	// Ensuring that the labels and images are fully loaded
	const dispatch = useDispatch();
	const [labelsAreLoaded, setLabelsAreLoaded] = useState(false);
	const [imagesAreLoaded, setImagesAreLoaded] = useState(false);

	// For loading the available labels
	useEffect(() => {
		if (!labelsAreLoaded) {
			dispatch(getLabelsForExplore()).then(() => setLabelsAreLoaded(true));
		}
	}, [dispatch, labelsAreLoaded, setLabelsAreLoaded]);
	const labelOptions = Object.values(useSelector(state => state.label));

	// For getting the user's input label or choosing a label for the user
	let label = useSelector(state => state.search_label);
	if (!label && labelsAreLoaded) {
		const indexChoice = Math.floor(Math.random() * labelOptions.length);
		label = labelOptions[indexChoice].name;
		dispatch(getSearchLabel(label))
	}

	// For loading the images with the specified label
	useEffect(() => {
		if (label) {
			dispatch(imageByLabel(label)).then(() => setImagesAreLoaded(true));
		}
	}, [dispatch, label, setImagesAreLoaded]);
	const images = Object.values(useSelector(state => state.image));

	// For getting the image detail that the user clicked
	useEffect(() => {
		if (detail) {
			dispatch(getImageById(detail));
		}
	}, [dispatch, detail]);

	return (
		imagesAreLoaded && images.length 
			?
				(
					<div className="grid" style={{ "--colNum": colNum }}>
						{images.map((image) => {
							return (
								<div key={image.id} style={{ cursor: "pointer" }}>
									<OpenModalImageItem
										modalComponent={
											<ImageModal id={detail} /> // Pass detail directly to the modal
										}
										src={image.url}
										alt={image.title ? image.title : "Image"}
										onItemClick={() => setDetail(image.id)} // Set detail on click
									/>
								</div>
							);
						})}
					</div>
				)
			:
				(
					<h1>No such image with label {`"${label}"`} found!</h1>
				)
	);
}

export default ExplorePage;
