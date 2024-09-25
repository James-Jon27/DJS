import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { getStashById, updateStashById } from "../../redux/stash";
import HomePage from "../HomePage";
import "./UploadStash.css";

export default function UpdateStash() {
	const nav = useNavigate();
	const dispatch = useDispatch();
	const { id } = useParams();
	const stash = useSelector((state) => state.stash);
	const [title, setTitle] = useState("");
	const [description, setDescription] = useState("");
	const [loading, setLoading] = useState(false);
    
	useEffect(() => {
		dispatch(getStashById(id));
	}, [dispatch, id]);

    useEffect(() => {
        if(stash) {
            setTitle(stash.name)
            setDescription(stash.description)
        }
    }, [stash])

	if (!stash) {
		return <h1 style={{ textAlign: "center" }}>Loading...</h1>;
	}

	const handleSubmit = async (e) => {
		e.preventDefault();

		const data = new FormData();
		data.append("name", title);
		data.append("description", description);

		setLoading(true);
		await dispatch(updateStashById(id, data));
		setLoading(false);
		nav(`/stashes/${id}`);

	};

	return (
		<div className="stash-create">
			<h1 style={{ textDecoration: "underline", fontSize: "3.5rem" }}>Update Your Stash</h1>
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
					Finish
				</button>
				{loading && <p>Loading...</p>}
			</form>
			<div className="your-future">
				<HomePage />
			</div>
		</div>
	);
}
