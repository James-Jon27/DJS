import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import "./UserProfilePostedImage.css";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";

function UserProfilePostedImage() {
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	useEffect(() => {
		function handleColNum() {
			setColNum(parseInt((window.innerWidth - 40) / 340));
		}

		window.addEventListener("resize", handleColNum);

		return () => window.removeEventListener("resize", handleColNum);
	}, []);

	const images = useSelector((state) => state.session.user.Images);

	return (
		<>
			<div className="grid" style={{ "--colNum": colNum }}>
				{images.map((image) => {
					return (
						<div key={image.id} style={{ cursor: "pointer" }}>
							<OpenModalImageItem
								modalComponent={<ImageModal id={image.id} />}
								src={image.url}
								alt={image.title ? image.title : "Image"}
							/>
						</div>
						// <img src={image.url} key={image.id} />
					);
				})}
			</div>
		</>
	);
}

export default UserProfilePostedImage;
