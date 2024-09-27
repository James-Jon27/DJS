import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import "./StashPage.css";
import { getFavoritesThunk } from "../../redux/favorites";
import { thunkGetUserById } from "../../redux/user";
import { favoriteImages } from "../../redux/image";

function FavoritesPage() {
    const navigate = useNavigate();
	const dispatch = useDispatch();
	const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340));
	const [isLoaded, setIsLoaded] = useState(false);
	const sessionUser = useSelector((state) => state.session.user);
	const favImg = useSelector((state) => state.image);
	const faves = Object.values(favImg)
    const user = useSelector(state => state.user)
	const { userId } = useParams();
	useEffect(() => {
		function handleColNum() {
			setColNum(parseInt((window.innerWidth - 40) / 340));
		}

		window.addEventListener("resize", handleColNum);

		return () => window.removeEventListener("resize", handleColNum);
	}, []);

	useEffect(() => {
		dispatch(thunkGetUserById(userId))
		dispatch(getFavoritesThunk(userId))
		dispatch(favoriteImages(userId))
		.then(() => setIsLoaded(true))
	}, [dispatch, userId]);


	if (!isLoaded) {
		return <h1>Loading...</h1>;
	}

    const owner = user

	return (
		isLoaded && (
			<div className="stashContainer">
				<div className="titleUser">
					<h1>{owner.username}&apos;s Favorites</h1>
				</div>
				<p id="description">Favorite Images</p>
				{faves && faves.length ? (
					<div className="grid" style={{ "--colNum": colNum }}>
						{faves.map((image) => {
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
