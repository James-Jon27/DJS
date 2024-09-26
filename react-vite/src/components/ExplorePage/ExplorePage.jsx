import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useSearchParams } from "react-router-dom";
import { getImageById, imageByLabel } from "../../redux/image";
import { getLabelsForExplore } from "../../redux/label";
import "./ExplorePage.css";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";

function ExplorePage() {
	
	// For organizing the loaded images
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	const [detail, setDetail] = useState(null);
	useEffect(() => {
		function handleColNum() {
			setColNum(parseInt((window.innerWidth - 40) / 340));
		}
		window.addEventListener("resize", handleColNum);
		return () => window.removeEventListener("resize", handleColNum);
	}, []);

	const dispatch = useDispatch();
	const [labelIsLoaded, setLabelIsLoaded] = useState(false);
	const [imageIsLoaded, setImageIsLoaded] = useState(false);
	const [searchParams] = useSearchParams()

	// For loading the available labels
	useEffect(() => {
		dispatch(getLabelsForExplore()).then(() => setLabelIsLoaded(true))
	}, [dispatch, setLabelIsLoaded])
	const labelOptions = Object.values(useSelector(state => state.label))

	// For getting the user's input label or choosing a label for the user
	let label = useRef(null)
	useEffect(() => {
		label.current = searchParams.get('label')
		if (label.current) {
			label.current = decodeURIComponent(label.current)
		}
		else if (labelIsLoaded) {
			const indexChoice = Math.floor(Math.random() * labelOptions.length)
			label.current = labelOptions[indexChoice].name
		}
	}, [labelIsLoaded, labelOptions, searchParams])

	// For loading the images with the specified label
	useEffect(() => {
		if (label.current) {
			dispatch(imageByLabel(label.current)).then(() => setImageIsLoaded(true))
		}
	}, [dispatch, setImageIsLoaded])
	const images = Object.values(useSelector(state => state.image))

	// For getting the image detail that the user clicked
	useEffect(() => {
		if (detail) {
			dispatch(getImageById(detail));
		}
	}, [dispatch, detail]);

	return (
		<div className="grid" style={{ "--colNum": colNum }}>
			{imageIsLoaded &&
				images.map((image) => {
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
	);
}

export default ExplorePage;
