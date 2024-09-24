import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { createStashThunk } from "../../redux/stash";
import "./UploadStash.css"

export default function UploadStash() {
	const nav = useNavigate();
	const dispatch = useDispatch();
	const [title, setTitle] = useState("");
	const [description, setDescription] = useState("");
	const [loading, setLoading] = useState(false);

	const handleSubmit = async (e) => {
		e.preventDefault();

		const data = new FormData();
		data.append("title", title);
		data.append("description", description);

		setLoading(true);
		await dispatch(createStashThunk(data));
		//TODO: Navigate to stash page
		nav("/");
	};

	return (
		<div className="stash-create">
			<h1 style={{ textDecoration: "underline", fontSize: "3.5rem" }}>Create A Stash</h1>
			<form className="stash-form" onSubmit={handleSubmit} encType="multipart/form-data">
				<label>
					Title
					<input
						className="stash-titf"
						type="text"
						value={title}
						onChange={(e) => {
							setTitle(e.target.value);
						}}
						required
					/>
				</label>
				<label>
					Description
					<textarea
						className="stash-desc"
						type="text"
						value={description}
						onChange={(e) => {
							setDescription(e.target.value);
						}}
					/>
				</label>
				<button className="stash-submit" type="submit">
					Create
				</button>
				{loading && <p>Loading...</p>}
			</form>
            <div className="your-future"></div>
		</div>
	);
}
