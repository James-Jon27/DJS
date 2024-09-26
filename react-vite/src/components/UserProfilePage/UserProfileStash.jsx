import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useParams } from "react-router-dom";

import { getUserStashes } from "../../redux/stash";

import "./UserProfileStash.css";

function UserProfileStash() {
	const [isLoaded, setIsLoaded] = useState(false)
	const { userId } = useParams()
	const dispatch = useDispatch()
	useEffect(() => {
		dispatch(getUserStashes(userId)).then(() => setIsLoaded(true))
	}, [dispatch, userId])
	const userStashes = Object.values(useSelector((state) => state.stash));

	return ( 
		isLoaded &&
			<div className="Stashes">
				<div className="Favorite">Favorites</div>
				{userStashes.map((stash) => {
					return (
						<NavLink key={stash.id} style={{textDecoration: "none", color: "black"}}to={`/stashes/${stash.id}`}>
							<div className="Stash">{stash.name}</div>
						</NavLink>
					);
				})}
			</div>
	);
}

export default UserProfileStash;
