import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import "./UserProfilePostedImage.css";
import { userImages } from "../../redux/image";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";
import { NavLink, useParams } from "react-router-dom";

function UserProfilePostedImage() {
	const dispatch = useDispatch();
	const { userId } = useParams();
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	const [isLoaded, setIsLoaded] = useState(false);
	const allImages = Object.values(useSelector((state) => state.image));

	const imgValues = Object.values(allImages);
	const images = imgValues.filter((image) => image.userId == userId);

	useEffect(() => {
		dispatch(userImages(userId)).then(() => setIsLoaded(true));
	}, [dispatch, userId]);

	useEffect(() => {
		function handleColNum() {
			setColNum(parseInt((window.innerWidth - 40) / 340));
		}
		window.addEventListener("resize", handleColNum);
		return () => window.removeEventListener("resize", handleColNum);
	}, []);

	if (images.length < 1) {
		return (
			<div className="Stashes">
				<NavLink style={{ textDecoration: "none", color: "black" }} to={`/images/new`}>
					<div className="Stash">No Images, Click to Create</div>
				</NavLink>
			</div>
		);
	}

	if (!isLoaded) {
		return <h1 style={{ textAlign: "center" }}>Loading...</h1>;
	}

	return (
		<div className="grid" style={{ "--colNum": colNum }}>
			{images.reverse().map((image) => {
				return (
					<div key={image.id}>
						<OpenModalImageItem
							style={{ cursor: "pointer" }}
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
