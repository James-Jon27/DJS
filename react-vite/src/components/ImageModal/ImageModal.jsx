import { useDispatch, useSelector } from "react-redux";
import { getImageById } from "../../redux/image";
import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { getImageComments, postComment } from "../../redux/comment";
import "./ImageModal.css";

export default function ImageModal({ id }) {
	const dispatch = useDispatch();
	const { closeModal } = useModal();
	const userStashes = useSelector((state) => state.session.user.Stashes);
	const sessionUser = useSelector((state) => state.session.user);
	const imageSelect = useSelector((state) => state.image);
	const commentSelect = useSelector((state) => state.comment);
	const comments = Object.values(commentSelect);
	const [loading, setLoading] = useState(true);
	const [image, setImage] = useState(null);
	const [checkedStashes, setCheckedStashes] = useState(new Set());
	const [comment, setComment] = useState("");

	useEffect(() => {
		const fetchAllData = async () => {
			setLoading(true);
			await dispatch(getImageById(id))
			await dispatch(getImageComments(id))
			const imageData = imageSelect[id]
			setImage(imageData)
			if (imageData) {
				const initStashSet = new Set(imageData.Stashes.map((stash) => stash.id))
				setCheckedStashes(initStashSet)
			}
			setLoading(false)
		}

		fetchAllData();
	}, [dispatch, id])

	const refetch = async () => {
		await dispatch(getImageById(id));
		await dispatch(getImageComments(id));
		const imageData = imageSelect[id];
		setImage(imageData);
	};

	const handleSubmit = async (e) => {
		e.preventDefault()
		const res =  await dispatch(postComment(image.id, comment))
		if(res) {
			refetch();
			setComment("")
		}
	}

	const drop = () => {
		document.getElementById("myDropdown").classList.toggle("show");
	};

	const checkbox = (stashId) => {
		const currChecks = new Set(checkedStashes);
		if (currChecks.has(stashId)) {
			currChecks.delete(stashId);
		} else {
			currChecks.add(stashId);
		}
		setCheckedStashes(currChecks);
	};

	if (loading || !image) {
		return <h1 style={{color: "white"}}>Loading...💥</h1>;
	}

	const owner = image.User;
	const faves = image.Favorites.length;

	return (
		<div className="imgPage">
			<div className="imgUser">
				<div className="img-modal">
					<img src={image.url} alt={image.title} />
				</div>
				<div className="userInt">
					<div className="prof">
						<NavLink className="circle-modal" to={`user/${owner.id}`} onClick={closeModal}>
							{owner.firstName[0]}
						</NavLink>
						<h2>{owner.username}</h2>
					</div>
					<div className="stashDropdown">
						<div className="dropdown">
							<button className="dropbtn" onClick={drop}>
								Add to Stash 👇
							</button>
							<div id="myDropdown" className="dropdown-content">
								{userStashes.map((stash) => {
									return (
										<label key={stash.id}>
											<input
												type="checkbox"
												checked={checkedStashes.has(stash.id)}
												onChange={() => checkbox(stash.id)}
											/>
											{stash.name}
										</label>
									);
								})}
							</div>
						</div>
					</div>
					<div>
						<button className="favorite">Favorite</button>
					</div>
				</div>
			</div>
			<span className="imgInfo">
				<div>
					{image.title && <h1>{image.title}</h1>}
					{image.description && <p>{image.description}</p>}
				</div>
				<h3>❤️ {faves} favorites</h3>
			</span>
			<span className="comments">
				<h3>Comments</h3>
				{sessionUser && sessionUser.id !== owner.id && (
					<form onSubmit={handleSubmit}>
						<textarea
							placeholder="Leave your comment here..."
							value={comment}
							onChange={(e) => setComment(e.target.value)}
						/>
						<button className="comment" type="submit" disabled={comment.length < 7}>
							Add a Comment
						</button>
					</form>
				)}
				{comments.map((comment) => (
					<div key={comment.id}>
						<h5>{comment.User.username}</h5>
						<p>{comment.comment}</p>
					</div>
				))}
			</span>
		</div>
	);
}
