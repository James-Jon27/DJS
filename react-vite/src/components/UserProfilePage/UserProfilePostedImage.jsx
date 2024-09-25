import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import "./UserProfilePostedImage.css";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";

function UserProfilePostedImage() {
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	// const [isLoading, setLoading] = useState(true);

	useEffect(() => {
		function handleColNum() {
			setColNum(parseInt((window.innerWidth - 40) / 340));
		}

		window.addEventListener("resize", handleColNum);

		return () => window.removeEventListener("resize", handleColNum);
	}, []);

    // // Loader function doesn't work
	// useEffect(() => {
	// 	const load = async () => {
	// 		const timer = setTimeout(() => {
	// 			setLoading(false);
	// 		}, 5000);
	// 		return () => clearTimeout(timer);
	// 	};
	// 	load();
	// }, []);

    const images = useSelector((state) => state.session.user.Images);
	
    // //Loader function
	// if (!images) {
	// 	return <h1 style={{textAlign:"center"}}>Loading...</h1>;
	// }

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
					);
				})}
			</div>
		</>
	);
}

export default UserProfilePostedImage;
