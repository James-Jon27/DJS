import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { createImage } from "../../redux/image";
import "./UploadImage.css";

const UploadImage = () => {
	const navigate = useNavigate(); // so that you can redirect after the image upload is successful
	const dispatch = useDispatch();
	const [image, setImage] = useState(null);
	const [title, setTitle] = useState("");
	const [description, setDescription] = useState("");
	const [labels, setLabels] = useState("");
	const [imageLoading, setImageLoading] = useState(false);

	const handleSubmit = async (e) => {
		e.preventDefault();
		const formData = new FormData();
		formData.append("image", image);
		formData.append("title", title);
		formData.append("description", description);
		formData.append("labels", labels);

		// aws uploads can be a bit slow—displaying
		// some sort of loading message is a good idea
		setImageLoading(true);
		await dispatch(createImage(formData));
        //TODO: navigate to user profile to view new image
		navigate("/");
	};

	return (
		<div className="img-create">
			<h1 style={{ textDecoration: "underline", fontSize: "3.5rem" }}>Create an Image</h1>
			<form className="img-form" onSubmit={handleSubmit} encType="multipart/form-data">
				<label>
					Title
					<input className="img-titf" type="text" value={title} onChange={(e) => setTitle(e.target.value)} required />
				</label>
				<label>
					Labels (Optional)
					<input className="img-lblf" type="text" value={labels} onChange={(e) => setLabels(e.target.value)} />
				</label>
				<label>
					Description (Optional)
					<textarea className="img-descf" type="text" value={description} onChange={(e) => setDescription(e.target.value)} />
				</label>
				<label>
					<input className="img-filef" type="file" accept="image/*" onChange={(e) => setImage(e.target.files[0])} />
				</label>
				<button className="img-submit" type="submit">Post</button>
				{imageLoading && <p style={{color: "white", fontSize: "1rem"}}>Loading...</p>}
			</form>
		</div>
	);
};

export default UploadImage;
