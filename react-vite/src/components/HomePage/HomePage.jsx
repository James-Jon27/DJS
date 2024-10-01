import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getImages } from "../../redux/image";
import "./HomePage.css";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";
import { getLabelsForExplore } from "../../redux/label";

function HomePage() {
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));

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
		dispatch(getLabelsForExplore())
		dispatch(getImages())
		setIsLoaded(true);
	}, [dispatch]);

	const images = Object.values(useSelector((state) => state.image));
	if(!isLoaded) {
		return (
			<h1 style={{ textAlign: "center" }}>Loading Images ...</h1>
		);
	}

	return (
		<div className="grid" style={{ "--colNum": colNum }}>
			{isLoaded &&
				images.map((image) => (
					<div key={image.id}>
						<OpenModalImageItem
							style={{ cursor: "pointer" }}
							modalComponent={
								<ImageModal id={image.id} /> // Pass detail directly to the modal
							}
							src={image.url}
							alt={image.title ? image.title : "Image"}
						/>
					</div>
				))}
		</div>
	);
}

export default HomePage;
