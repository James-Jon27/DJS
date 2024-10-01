import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { createStashThunk } from "../../redux/stash";
import "./UploadStash.css";

export default function UploadStash() {
	const nav = useNavigate();
	const dispatch = useDispatch();
	const sessionUser = useSelector((state) => state.session.user);
	const [title, setTitle] = useState("");
	const [description, setDescription] = useState("");
	const [loading, setLoading] = useState(false);

	const handleSubmit = async (e) => {
		e.preventDefault();

		const data = new FormData();
		data.append("name", title);
		data.append("description", description);

		setLoading(true);
		const res = await dispatch(createStashThunk(data));
		//TODO: Navigate to stash page
		if (res.id) {
			dispatch()
			setLoading(false);
			nav(`/stashes/${res.id}`);
		} else {
			return await res.json();
		}
	};

	const disabled = () => {
		if (
			!sessionUser ||
			title.length > 30 ||
			title.length < 1 ||
			(description && description.length > 150)
		) {
			return true;
		} else return false;
	};

	return (
		<div className="stash-create">
			<h1 style={{ textDecoration: "underline", fontSize: "3.5rem" }}>Create A Stash</h1>
			<form className="stash-form" onSubmit={handleSubmit} encType="multipart/form-data">
				<label>
					Title
					{title.length > 30 && (
						<p style={{ color: "red", fontSize: "1rem" }}>
							Title can not be more than 30 characters
						</p>
					)}
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
					{description && description.length > 150 && (
						<p style={{ color: "red", fontSize: "1rem" }}>
							Description can not be more than 150 characters
						</p>
					)}
					<textarea
						className="stash-desc"
						type="text"
						value={description}
						onChange={(e) => {
							setDescription(e.target.value);
						}}
					/>
				</label>
				{!sessionUser && (
					<p style={{ color: "red", fontWeight: "bold" }}>Please Log In to Create!</p>
				)}
				<button className="stash-submit" type="submit" disabled={disabled()}>
					Create
				</button>
				{loading && <p>Loading...</p>}
			</form>
			<div className="your-future">
			</div>
		</div>
	);
}
