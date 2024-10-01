import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { deleteStashById, getStashById } from "../../redux/stash";
import { MdDeleteForever } from "react-icons/md";
import { FaEdit } from "react-icons/fa";
import { FaCheck } from "react-icons/fa";
import { GiCancel } from "react-icons/gi";
import "./StashPage.css";
import OpenModalImageItem from "../ImageModal/OpenModalImageItem";
import ImageModal from "../ImageModal/ImageModal";

function StashPage() {
	const dispatch = useDispatch();
	const { id: stashId } = useParams();
	const navigate = useNavigate();
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	const sessionUser = useSelector((state) => state.session.user);
	const stash = useSelector((state) => state.stash);
	const [isLoaded, setIsLoaded] = useState(false);
	const [deleteConfirm, setDeleteConfirm] = useState(false);

	useEffect(() => {
		function handleColNum() {
			setColNum(parseInt((window.innerWidth - 40) / 340));
		}

		window.addEventListener("resize", handleColNum);

		return () => window.removeEventListener("resize", handleColNum);
	}, []);

	useEffect(() => {
		dispatch(getStashById(stashId)).then(() => setIsLoaded(true));
	}, [dispatch, stashId]);

	const handleDelete = async (e) => {
		e.preventDefault();
		await dispatch(deleteStashById(stashId));
		navigate(`/user/${sessionUser.id}/stashes`);
	};

	const handleEdit = async (e) => {
		e.preventDefault();
		navigate(`/stashes/${stashId}/edit`);
	};

	const deleteConfirmationToggle = (confirmation) => {
		if (confirmation) {
			return (
				<div style={{ display: "flex", paddingTop: "25px" }}>
					<button
						onClick={(e) => handleDelete(e)}
						style={{
							border: "solid 2px red",
							cursor: "pointer",
							background: "#943B0A",
							marginRight: "10px",
						}}>
						<FaCheck style={{ height: "35px", width: "35px" }} />
					</button>
					<button
						onClick={() => setDeleteConfirm(false)}
						style={{
							border: "solid 2px red",
							cursor: "pointer",
							background: "#943B0A",
							marginLeft: "10px",
						}}>
						<GiCancel style={{ height: "35px", width: "35px" }} />
					</button>
				</div>
			);
		} else {
			return (
				<div style={{ display: "flex", paddingTop: "25px" }}>
					<button
						onClick={() => setDeleteConfirm(true)}
						style={{
							border: "solid 2px red",
							cursor: "pointer",
							background: "#943B0A",
							marginRight: "10px",
						}}>
						<MdDeleteForever style={{ height: "35px", width: "35px" }} />
					</button>
					<button
						onClick={(e) => handleEdit(e)}
						style={{
							border: "solid 2px red",
							cursor: "pointer",
							background: "#943B0A",
							marginLeft: "10px",
						}}>
						<FaEdit style={{ height: "35px", width: "35px" }} />
					</button>
				</div>
			);
		}
	};

	if (!stash || !isLoaded) {
		return <h1 style={{textAlign: "center"}}>Loading...</h1>;
	}

	const owner = stash.User;

	return (
		isLoaded && (
			<div className="stashContainer">
				<div className="titleUser">
					<h1>{stash.name}</h1>
					<p>- by {stash.User.username}</p>
				</div>
				<p id="description">{stash.description}</p>
				{deleteConfirm && <p>Are you sure?</p>}
				{sessionUser && sessionUser.id == owner.id && deleteConfirmationToggle(deleteConfirm)}
				{stash.Images.length ? (
					<div className="grid" style={{ "--colNum": colNum }}>
						{stash.Images.map((image) => {
							return (
								<div key={image.id}>
									<OpenModalImageItem
										style={{ cursor: "pointer" }}
										modalComponent={<ImageModal id={image.id} />}
										src={image.url}
										alt={image.title ? image.title : "Image"}
									/>
								</div>
							);
						})}
					</div>
				) : (
					<div className="emptyStashBox">
						<h1>No Images Stashed</h1>
						{sessionUser && sessionUser.id == owner.id && (
							<button style={{ cursor: "pointer" }} onClick={() => navigate(`/explore`)}>
								Go stash some!
							</button>
						)}
					</div>
				)}
			</div>
		)
	);
}

export default StashPage;
