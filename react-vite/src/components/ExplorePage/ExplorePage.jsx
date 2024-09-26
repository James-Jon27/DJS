import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getImageById, getImages } from "../../redux/image";
import "./ExplorePage.css";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";

function ExplorePage() {
	
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
	const [isLoaded, setIsLoaded] = useState(false);
	useEffect(() => {
		dispatch(getImages()).then(() => setIsLoaded(true));
	}, [dispatch]);
	const images = Object.values(useSelector((state) => state.image));

		useEffect(() => {
			if (detail) {
				dispatch(getImageById(detail));
			}
		}, [dispatch, detail]);
	return (
		<div className="grid" style={{ "--colNum": colNum }}>
			{isLoaded &&
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
