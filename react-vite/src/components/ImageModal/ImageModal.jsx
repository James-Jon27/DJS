import { useDispatch, useSelector } from "react-redux";
import { getImageById } from "../../redux/image";
import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { getImageComments } from "../../redux/comment";
import "./ImageModal.css";
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import CommentModal from "../CommentModal/CommentModal";

export default function ImageModal({ id }) {
	const dispatch = useDispatch();
	const {closeModal} = useModal()
	const sessionUser = useSelector((state) => state.session.user);
	const userStashes = useSelector((state) => state.session.user.Stashes);
	const imageSelect = useSelector((state) => state.image);
	const commentSelect = useSelector(state => state.comment)
	const comments = Object.values(commentSelect)
	const image = imageSelect[id];

	const [checkedStashes, setCheckedStashes] = useState(new Set());

	useEffect(() => {
		dispatch(getImageById(id));
	}, [dispatch, id]);

	useEffect(() => {
		if (image) {
			const initStashSet = new Set(image.Stashes.map((stash) => stash.id));
			setCheckedStashes(initStashSet);
		}

		if(image) {
			dispatch(getImageComments(id))
		}

	}, [image, dispatch, id]);

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

	const refetch = async (id) => {
		await dispatch(getImageComments(id))
	} 

	if (!image || !comments) {
		return <h1>💥</h1>;
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
				{sessionUser && sessionUser.id !== owner.id && <OpenModalButton className="comment" buttonText="Add a Comment" modalComponent={<CommentModal image={image.id}/>} onModalClose={refetch(image.id)} />}
				<button className="comment">Add a Comment</button>
				{comments &&
					comments.map((comment) => {
						return (
							<div key={comment.id}>
								<h5>{comment.User.username}</h5>
								<p>{comment.comment}</p>
							</div>
						);
					})}
			</span>
		</div>
	);
}
