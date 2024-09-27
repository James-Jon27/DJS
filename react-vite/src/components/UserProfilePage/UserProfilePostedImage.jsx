import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import "./UserProfilePostedImage.css";
import { userImages } from "../../redux/image";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";
import { useParams } from "react-router-dom";

function UserProfilePostedImage() {
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	const [isLoaded, setIsLoaded] = useState(false)
	const { userId } = useParams()
	const dispatch = useDispatch()
	
	useEffect(() => {
		dispatch(userImages(userId)).then(() => setIsLoaded(true))
	}, [dispatch, userId])

	useEffect(() => {
		function handleColNum() {
			setColNum(parseInt((window.innerWidth - 40) / 340));
		}
		window.addEventListener("resize", handleColNum);
		return () => window.removeEventListener("resize", handleColNum);
	}, []);

    const images = Object.values(useSelector((state) => state.image));

	return (
		isLoaded && 
			<div className="grid" style={{ "--colNum": colNum }}>
				{images.reverse().map((image) => {
					return (
						<div key={image.id} style={{ cursor: "pointer" }}>
							<OpenModalImageItem
								modalComponent={<ImageModal id={image.id} />}
								src={image.url}
								alt={image.title ? image.title : "Image"}
							/>
						</div>
					);
				})}
			</div>
	);
}

export default UserProfilePostedImage;
