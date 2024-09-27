import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import "./StashPage.css";
import { getFavoritesThunk } from "../../redux/favorites";

function FavoritesPage() {
    const navigate = useNavigate();
	const dispatch = useDispatch();
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	const [isLoaded, setIsLoaded] = useState(false);
	const sessionUser = useSelector((state) => state.session.user);
	const faves = useSelector((state) => state.favorites);
	const { userId } = useParams();
    console.log(userId)

	useEffect(() => {
		function handleColNum() {
			setColNum(parseInt((window.innerWidth - 40) / 340));
		}

		window.addEventListener("resize", handleColNum);

		return () => window.removeEventListener("resize", handleColNum);
	}, []);

	useEffect(() => {
		dispatch(getFavoritesThunk(userId))
	}, [dispatch, userId]);


	if (!faves) {
		return <h1>Loading...</h1>;
	}

    const owner = faves.Users

	return (
		isLoaded && (
			<div className="stashContainer">
				<div className="titleUser">
					<h1>User&apos;s Favorites</h1>
				</div>
				<p id="description">Favorite Images</p>
				{!faves || faves.Images.length ? (
					<div className="grid" style={{ "--colNum": colNum }}>
						{faves.Images.map((image) => {
							return <img src={image.url} key={image.id} />;
						})}
					</div>
				) : (
					<div className="emptyStashBox">
						<h1>No Favorite Images</h1>
						{sessionUser && sessionUser.id == owner.id && (
							<button style={{ cursor: "pointer" }} onClick={() => navigate(`/explore`)}>
								Go like some!
							</button>
						)}
					</div>
				)}
			</div>
		)
	);
}

export default FavoritesPage;
