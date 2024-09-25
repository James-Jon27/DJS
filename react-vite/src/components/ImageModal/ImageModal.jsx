import { useDispatch, useSelector } from "react-redux";
import { getImageById } from "../../redux/image";
import { useEffect } from "react";
import { UserProfileLayout } from "../UserProfilePage";
import { NavLink } from "react-router-dom";

export default function ImageModal({ id }) {
	const dispatch = useDispatch();
	const image = useSelector(state => state.image);

	useEffect(() => {
		dispatch(getImageById(id));
	}, [dispatch, id]);
    const user = image[id].User
    // const comments = image.Comments
    console.log(image)
    console.log("User", user)

	return (
		<div className="imgPage">
			<div className="imgUser">
				<div className="img-modal">
                    <img src={image.url} alt={image.title}/>
                </div>
				<div className="userInt">
					<div className="prof">
                        {/* <NavLink className="circle">{image.user.firstName[0]}</NavLink> */}
                    </div>
					<div className="stashDropdown"></div>
					<div className="favorite"></div>
				</div>
			</div>
			<span className="imgInfo"></span>
			<span className="comments"></span>
		</div>
	);
}
