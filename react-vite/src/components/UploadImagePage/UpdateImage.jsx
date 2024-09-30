import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { getImageById, updateImage } from "../../redux/image";
import "./UploadImage.css";

const UpdateImage = () => {
	const navigate = useNavigate(); // so that you can redirect after the image upload is successful
	const dispatch = useDispatch();
	const { id } = useParams();
	const imageSelect = useSelector((state) => state.image);
	const sessionUser = useSelector((state) => state.session.user);
	const img = imageSelect[id];
	const [title, setTitle] = useState("");
	const [description, setDescription] = useState("");
	const [labels, setLabels] = useState("");
	const [imageLoading, setImageLoading] = useState(false);

	useEffect(() => {
		dispatch(getImageById(id));
	}, [dispatch, id]);

	useEffect(() => {
		if (img) {
			setTitle(img.title);
			if (img.description !== "null") {
				setDescription(img.description);
			}
			// TODO: Sukh work your magic
			const imgLabels = img.Labels.map((label, el) => img.Labels[el].name);
			setLabels(imgLabels);
		}
	}, [img]);

	if (!img) {
		return <h1 style={{ textAlign: "center" }}>Loading...</h1>;
	}

	const handleSubmit = async (e) => {
		e.preventDefault();
		const formData = new FormData();
		formData.append("title", title);
		formData.append("description", description);
		formData.append("labels", labels);

		// aws uploads can be a bit slow—displaying
		// some sort of loading message is a good idea
		setImageLoading(true);
		await dispatch(updateImage(id, formData));
		//TODO: navigate to user profile to view new image
		navigate(`/user/${sessionUser.id}/posted-images`);
	};

	const disabled = () => {
		if (
			(description && description.length > 250) ||
			title.length > 50 ||
			title.length < 1 ||
			(labels && labels.length > 50)
		) {
			return true;
		}
		return false;
	};

	return (
		<div className="img-create">
			<h1 style={{ textDecoration: "underline", fontSize: "3.5rem" }}>Update Your Image</h1>
			<form className="img-form" onSubmit={handleSubmit} encType="multipart/form-data">
				<label>
					Title
					{title.length > 49 && (
						<p style={{ color: "red", fontSize: "1rem" }}>
							Title can not be more than 50 characters
						</p>
					)}
					<input
						className="img-titf"
						type="text"
						value={title}
						onChange={(e) => setTitle(e.target.value)}
						required
					/>
				</label>
				<label>
					Labels (Separated by Comma)
					{labels && labels.length > 49 && (
						<p style={{ color: "red", fontSize: "1rem" }}>
							A label can not be more than 50 characters
						</p>
					)}
					<input
						className="img-lblf"
						type="text"
						value={labels}
						onChange={(e) => setLabels(e.target.value)}
					/>
				</label>
				<label>
					Description (Optional)
					{description && description.length > 250 && (
						<p style={{ color: "red", fontSize: "1rem" }}>
							Description can not be more than 255 characters
						</p>
					)}
					<textarea
						className="img-descf"
						type="text"
						value={description}
						onChange={(e) => setDescription(e.target.value)}
					/>
				</label>
				<button className="img-submit" type="submit" disabled={disabled()}>
					Update
				</button>
				{imageLoading && <p style={{ color: "white", fontSize: "1rem" }}>Loading...</p>}
			</form>
		</div>
	);
};

export default UpdateImage;
