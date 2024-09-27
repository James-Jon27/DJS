import { useDispatch, useSelector } from "react-redux";
import { deleteImage, getImageById, userImages } from "../../redux/image";
import { useEffect, useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { getImageComments, postComment } from "../../redux/comment";
import { MdDeleteForever } from "react-icons/md";
import { FaEdit } from "react-icons/fa";
import "./ImageModal.css";

export default function ImageModal({ id }) {
	const dispatch = useDispatch();
	const nav = useNavigate();
	const { closeModal } = useModal();
	const sessionUser = useSelector((state) => state.session.user);
	const imageSelect = useSelector((state) => state.image);
	const commentSelect = useSelector((state) => state.comment);
	const comments = Object.values(commentSelect);
	const [loading, setLoading] = useState(true);
	const [image, setImage] = useState(null);
	const [checkedStashes, setCheckedStashes] = useState(new Set());
	const [comment, setComment] = useState("");

	let userStashes;
	if (sessionUser) {
		userStashes = sessionUser.Stashes;
	}

	useEffect(() => {
		const fetchAllData = async () => {
			setLoading(true);
			await dispatch(getImageById(id));
			await dispatch(getImageComments(id));
			const imageData = imageSelect[id];
			setImage(imageData);
			if (imageData) {
				const initStashSet = new Set(imageData.Stashes.map((stash) => stash.id));
				setCheckedStashes(initStashSet);
			}
			setLoading(false);
		};

		fetchAllData();
	}, [dispatch, id, imageSelect]);

	const refetch = async () => {
		// await dispatch(getImageById(id));
		await dispatch(getImageComments(id));
		const imageData = imageSelect[id];
		setImage(imageData);
	};

	const handleCommentSubmit = async (e) => {
		e.preventDefault();
		const form = new FormData()
		form.append("comment", comment)
		const res = await dispatch(postComment(image.id, form));

		if (res) {
			refetch();
			setComment("");
		}
	};

	const handleDelete = async (e) => {
		e.preventDefault();
		await dispatch(deleteImage(id));
		closeModal();
		await dispatch(userImages(sessionUser.id))
	};

	const handleEdit = async (e) => {
		e.preventDefault()
		closeModal()
		nav(`/images/${id}/edit`)
	};

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
		return <h1 style={{ color: "white" }}>Loading...💥</h1>;
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
						{sessionUser.id == owner.id && (
							<div style={{ display: "flex" }}>
								<button
									onClick={handleDelete}
									style={{ cursor: "pointer", background: "none", border: "none" }}>
									<MdDeleteForever style={{ height: "35px", width: "35px" }} />
								</button>
								<button
									onClick={handleEdit}
									style={{ cursor: "pointer", background: "none", border: "none" }}>
									<FaEdit style={{ height: "35px", width: "35px" }} />
								</button>
							</div>
						)}
					</div>
					<div className="stashDropdown">
						{sessionUser && (
							<div className="dropdown">
								<button style={{ cursor: "pointer" }} className="dropbtn" onClick={drop}>
									Add to Stash 👇
								</button>
								{/* TODO: WORK */}
								{userStashes.length > 0 ? (
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
								) : (
									<div id="myDropdown" className="dropdown-content">
										<label style={{ textAlign: "center" }}>No User Stashes</label>
									</div>
								)}
							</div>
						)}
					</div>
					{sessionUser && (
						// TODO: Favorite
						<div>
							<button style={{ cursor: "pointer" }} className="favorite">
								Favorite
							</button>
						</div>
					)}
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
					<form onSubmit={handleCommentSubmit}>
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
				{comments.reverse().map((comment) => (
					<div key={comment.id}>
						<h5>{comment.User.username}</h5>
						<p>{comment.comment}</p>
					</div>
				))}
			</span>
		</div>
	);
}
