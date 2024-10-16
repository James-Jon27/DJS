import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { imageByLabel } from "../../redux/image";
import { getLabelsForExplore } from "../../redux/label";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";
import { getSearchLabel } from "../../redux/searchLabel";
import "./ExplorePage.css";

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
	// TODO: Find only labels with images, NOT COMPLETE
	useEffect(() => {
		if (!labelsAreLoaded) {
			dispatch(getLabelsForExplore()).then(() => setLabelsAreLoaded(true));
		}
	}, [dispatch, labelsAreLoaded, setLabelsAreLoaded]);
	const labelOptions = Object.values(useSelector((state) => state.label));

	// For getting the user's input label or choosing a label for the user
	const labelFromState = useSelector((state) => state.search_label);
	let label = labelFromState;
	if (!label && labelsAreLoaded) {
		const indexChoice = Math.floor(Math.random() * (6 - 0) + 0);
		label = labelOptions[indexChoice].name;
	}

	// If the user's input label is empty in state, then fill it in with a random available label
	// For loading the images with the specified label
	useEffect(() => {
		setImagesAreLoaded(false)
		if (label) {
			if (!labelFromState) {
				dispatch(getSearchLabel(label));
			}
			dispatch(imageByLabel(label)).then(() => setImagesAreLoaded(true));
		}
	}, [dispatch, label, labelFromState, setImagesAreLoaded]);

	const images = Object.values(useSelector((state) => state.image));

	if (!imagesAreLoaded) {
		return <h1 style={{ textAlign: "center" }}>Loading Images with the &quot;{label}&quot; label...</h1>;
	}

	return images.length ? (
		<div className="grid" style={{ "--colNum": colNum }}>
			{images.map((image) => {
				return (
					<div key={image.id}>
						<OpenModalImageItem
							style={{ cursor: "pointer" }}
							modalComponent={
								<ImageModal id={image.id} />
							}
							src={image.url}
							alt={image.title ? image.title : "Image"}
						/>
					</div>
				);
			})}
		</div>
	) : (
		<h1>No such image with label {`"${label}"`} found!</h1>
	);
}

export default ExplorePage;
