import { useDispatch, useSelector } from "react-redux";
import { deleteImage, getImageById, userImages } from "../../redux/image";
import { useEffect, useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { deleteComment, getImageComments, postComment } from "../../redux/comment";
import { MdDeleteForever } from "react-icons/md";
import { FaEdit, FaCheck } from "react-icons/fa";
import { GiCancel } from "react-icons/gi";
import "./ImageModal.css";
import { addFavToUser, delFavFromUser, getFavoritesThunk } from "../../redux/favorites";
import { getUserStashes, stashAnImage, unStashAnImage } from "../../redux/stash";
import { thunkGetUserById } from "../../redux/user";

function ImageModal({ id }) {
	const dispatch = useDispatch();
	const nav = useNavigate();
	const { closeModal } = useModal();
	const sessionUser = useSelector((state) => state.session.user);
	const imageSelect = useSelector((state) => state.image);
	const commentSelect = useSelector((state) => state.comment);
	const userFaves = useSelector((state) => state.favorite);
	const stashed = useSelector((state) => state.stash);
	const stashes = Object.values(stashed);
	const comments = Object.values(commentSelect);
	const [loading, setLoading] = useState(true);
	const [image, setImage] = useState(null);
	const [checkedStashes, setCheckedStashes] = useState(new Set());
	const [comment, setComment] = useState("");
	const [favoriteCheck, setFavoriteCheck] = useState(false);
	const [faveCount, setFaveCount] = useState(0);
	const [confirmDeleteId, setConfirmDeleteId] = useState(null);
	const [confirmDelete, setConfirmDelete] = useState(false)
	const [favLoad, setFavLoad] = useState(false)

	useEffect(() => {
		const fetchAllData = async () => {
			setLoading(true);
			await dispatch(getImageById(id));
			await dispatch(getImageComments(id));
			const imageData = imageSelect[id];

			if (imageData) {
				setImage(imageData);
				const initStashSet = new Set(
					imageData.Stashes.map((stash) => {
						if (!stash.errors) {
							stash.id;
						} else return;
					})
				);
				setCheckedStashes(initStashSet);
			}
			setLoading(false);
		};

		if (id) {
			fetchAllData();
		}
	}, [dispatch, id]);

	useEffect(() => {
		if (sessionUser) {
			dispatch(getUserStashes(sessionUser.id));
		}
	}, [dispatch, sessionUser]);

	useEffect(() => {
		if (image && sessionUser) {
			const isFavorite = image.Favorites.some((fav) => fav.user_id === sessionUser.id);
			setFavoriteCheck(isFavorite);
			setFaveCount(image.Favorites.length);
		}
	}, [sessionUser, image]);

	const refetch = async () => {
		if (image) {
			await dispatch(getImageComments(image.id));
		}
	};

	const handleCommentSubmit = async (e) => {
		e.preventDefault();
		const form = new FormData();
		form.append("comment", comment);
		const res = await dispatch(postComment(image.id, form));

		if (res) {
			refetch();
			setComment("");
		}
	};

	const deleteCommentHandler = async (commentId) => {
		try {
			await dispatch(deleteComment(commentId));
			refetch();
		} catch (error) {
			console.error("Error deleting comment:", error);
		}
	};

	const handleDelete = async (e) => {
		e.preventDefault();
		await dispatch(deleteImage(id));
		closeModal();
		await dispatch(userImages(sessionUser.id));
	};

	const handleEdit = async (e) => {
		e.preventDefault();
		closeModal();
		nav(`/images/${id}/edit`);
	};

	const drop = () => {
		document.getElementById("myDropdown").classList.toggle("show");
	};

	const checkbox = (stashId) => {
		const currChecks = new Set(checkedStashes);
		if (currChecks.has(stashId)) {
			currChecks.delete(stashId);
			uncheckStash(stashId);
		} else {
			currChecks.add(stashId);
			checkStash(stashId);
		}
		setCheckedStashes(currChecks);
	};

	const checkStash = async (stashId) => {
		if (!sessionUser) return;

		const alreadyThere = checkedStashes.has(image.id);
		if (!alreadyThere) {
			await dispatch(stashAnImage(image.id, stashId));
			await dispatch(thunkGetUserById(sessionUser.id));
		}
	};

	const uncheckStash = async (stashId) => {
		if (!sessionUser) return;

		const alreadyThere = checkedStashes.has(image.id);
		if (alreadyThere) {
			await dispatch(unStashAnImage(image.id, stashId));
			await dispatch(thunkGetUserById(sessionUser.id));
		}
	};

	const favoriteToggle = async (e) => {
		setFavLoad(true)
		e.preventDefault();
		if (sessionUser) {
			const existingFavorite = Object.values(userFaves).find((fav) => fav.image_id === image.id);
			if (existingFavorite) {
				await dispatch(delFavFromUser(existingFavorite.id));
				setFaveCount((prevCount) => prevCount - 1);
				setFavoriteCheck(false);
			} else {
				await dispatch(addFavToUser(image.id));
				setFaveCount((prevCount) => prevCount + 1);
				setFavoriteCheck(true);
			}

			await dispatch(getFavoritesThunk(sessionUser.id));
		}
		setFavLoad(false)
	};

	const handleClickOutside = () => {
		if (confirmDeleteId) {
			setConfirmDeleteId(null);
		}
	};

	const deleteConfirm = (id) => {
		if (confirmDeleteId === id) {
			return (
				<div>
					<button
						className="delete"
						style={{ height: "58px", width: "60px", marginRight: "10px" }}
						onClick={() => {
							deleteCommentHandler(id);
						}}>
						Confirm
					</button>
					<button
						className="delete"
						style={{ height: "58px", width: "58px", marginLeft: "10px" }}
						onClick={() => {
							setConfirmDeleteId(null);
						}}>
						Cancel
					</button>
				</div>
			);
		} else {
			return (
				<button
					className="delete"
					onClick={() => {
						setConfirmDeleteId(id);
					}}>
					Delete
				</button>
			);
		}
	};

	const deleteMe = (bool) => {
		if(bool) {
			return (
				<div style={{ display: "flex" }}>
					<button
						onClick={(e) => handleDelete(e)}
						style={{ cursor: "pointer", background: "none", border: "none" }}>
						<FaCheck style={{ height: "35px", width: "35px" }} />
					</button>
					<button
						onClick={() => setConfirmDelete(false)}
						style={{ cursor: "pointer", background: "none", border: "none" }}>
						<GiCancel style={{ height: "35px", width: "35px" }} />
					</button>
				</div>
			);
		} else {
			return (
				<div style={{ display: "flex" }}>
					<button
						onClick={() => setConfirmDelete(true)}
						style={{ cursor: "pointer", background: "none", border: "none" }}>
						<MdDeleteForever style={{ height: "35px", width: "35px" }} />
					</button>
					<button
						onClick={(e) => handleEdit(e)}
						style={{ cursor: "pointer", background: "none", border: "none" }}>
						<FaEdit style={{ height: "35px", width: "35px" }} />
					</button>
				</div>
			);
		}
	}

	if (loading || !image) {
		return <h1 style={{ color: "white" }}>Loading...💥</h1>;
	}

	const owner = image.User;
	const labels = image.Labels.map((label, el) => image.Labels[el].name);

	return (
		<div className="imgPage" onClick={handleClickOutside}>
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
						{sessionUser && sessionUser.id == owner.id && deleteMe(confirmDelete)}
					</div>
					<div className="stashDropdown">
						{sessionUser && (
							<div className="dropdown">
								<button style={{ cursor: "pointer" }} className="dropbtn" onClick={drop}>
									Add to Stash 👇
								</button>
								{stashes && stashes.length > 0 && stashes[0] !== "Stashes not found" ? (
									<div id="myDropdown" className="dropdown-content">
										{stashes.map((stash) => {
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
							<button
								onClick={favoriteToggle}
								disabled={favLoad}
								style={
									favoriteCheck
										? { cursor: "pointer", background: "#DB570F" }
										: { cursor: "pointer" }
								}
								className="favorite">
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
				<div>
					<h3>❤️ {faveCount} Favorites</h3>
					<div style={{ display: "flex", gap: "10px" }}>
						{labels &&
							labels.map((label, el) => {
								if (label !== "undefined") {
									return <h4 key={el}>{label}</h4>;
								}
							})}
					</div>
				</div>
			</span>
			<span className="comments">
				<h3>Comments</h3>
				{comment.length > 250 && (
					<p style={{ color: "red" }}>Comments should be less than 255 characters</p>
				)}
				{sessionUser && sessionUser.id !== owner.id && (
					<form onSubmit={handleCommentSubmit}>
						<textarea
							placeholder="Leave your comment here..."
							value={comment}
							onChange={(e) => setComment(e.target.value)}
						/>
						<button className="comment" type="submit" disabled={comment.length > 250}>
							Add a Comment
						</button>
					</form>
				)}
				{comments.reverse().map((comment) => (
					<div
						style={{ display: "flex", justifyContent: "space-between", marginTop: "10px" }}
						key={comment.id}>
						<div className="content">
							<h5>{comment.User.username}</h5>
							<p>{comment.comment}</p>
						</div>
						{sessionUser && sessionUser.id === comment.User.id && deleteConfirm(comment.id)}
					</div>
				))}
			</span>
		</div>
	);
}

export default ImageModal;
