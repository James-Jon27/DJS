import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { deleteStashById, getStashById } from "../../redux/stash";
import { MdDeleteForever } from "react-icons/md";
import { FaEdit } from "react-icons/fa";
import "./StashPage.css";

function StashPage() {
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	const sessionUser = useSelector((state) => state.session.user);
	const stash = useSelector((state) => state.stash);
	const { id: stashId } = useParams();
	const dispatch = useDispatch();
	const [isLoaded, setIsLoaded] = useState(false);

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

	const navigate = useNavigate();
	const handleDelete = async (e) => {
		e.preventDefault();
		await dispatch(deleteStashById(stashId));
		navigate(`/user/${sessionUser.id}/stashes`);
	};

	const handleEdit = async (e) => {
		e.preventDefault();
		navigate(`/stashes/${stashId}/edit`);
	};

	if(!stash){
		return <h1>Loading...</h1>
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
				{sessionUser && sessionUser.id == owner.id && (
					<div style={{ display: "flex", paddingTop: "25px" }}>
						<button
							onClick={handleDelete}
							style={{
								border: "solid 2px red",
								cursor: "pointer",
								background: "none",
								marginRight: "10px",
							}}>
							<MdDeleteForever style={{ height: "35px", width: "35px" }} />
						</button>
						<button
							onClick={handleEdit}
							style={{
								border: "solid 2px red",
								cursor: "pointer",
								background: "none",
								marginLeft: "10px",
							}}>
							<FaEdit style={{ height: "35px", width: "35px" }} />
						</button>
					</div>
				)}
				{stash.Images.length ? (
					<div className="grid" style={{ "--colNum": colNum }}>
						{stash.Images.map((image) => {
							return <img src={image.url} key={image.id} />;
						})}
					</div>
				) : (
					<div className="emptyStashBox">
						<h1>No Images Stashed</h1>
						{sessionUser && sessionUser.id == owner.id && (
							<button style={{cursor: "pointer"}}onClick={() => navigate(`/explore`)}>Go stash some!</button>
						)}
					</div>
				)}
			</div>
		)
	);
}

export default StashPage;
