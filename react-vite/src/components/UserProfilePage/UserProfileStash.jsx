import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useParams } from "react-router-dom";

import { getUserStashes } from "../../redux/stash";

import "./UserProfileStash.css";

function UserProfileStash() {
	const [isLoaded, setIsLoaded] = useState(false);
	const { userId } = useParams();
	const dispatch = useDispatch();

	useEffect(() => {
		dispatch(getUserStashes(userId));
		setIsLoaded(true);
	}, [dispatch, userId]);

	const userStashes = Object.values(useSelector((state) => state.stash));

	if (!isLoaded) {
		return <h1 style={{ textAlign: "center" }}>Loading...</h1>;
	}

	if (userStashes[0] === "Stashes not found" || !userStashes[0]) {
		return (
			isLoaded && (
				<div className="Stashes">
					<NavLink
						style={{ textDecoration: "none", color: "black" }}
						to={`/user/${userId}/favorites`}>
						<div className="Favorite">Favorites</div>
					</NavLink>
					<NavLink style={{ textDecoration: "none", color: "black" }} to={`/stashes/new`}>
						<div className="Stash">No Stashes, Click to Create</div>
					</NavLink>
				</div>
			)
		);
	} else {
		return (
			isLoaded && (
				<div className="Stashes">
					<NavLink
						style={{ textDecoration: "none", color: "black" }}
						to={`/user/${userId}/favorites`}>
						<div className="Favorite">Favorites</div>
					</NavLink>
					{userStashes.map((stash) => {
						return (
							<NavLink
								key={stash.id}
								style={{ textDecoration: "none", color: "black" }}
								to={`/stashes/${stash.id}`}>
								<div className="Stash">{stash.name}</div>
							</NavLink>
						);
					})}
				</div>
			)
		);
	}
}

export default UserProfileStash;
