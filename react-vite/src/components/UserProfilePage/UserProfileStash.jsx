import { useSelector } from "react-redux";
import "./UserProfileStash.css";
import { NavLink } from "react-router-dom";

function UserProfileStash() {
	const userStashes = useSelector((state) => state.session.user.Stashes);

	return (
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
