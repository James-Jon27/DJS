import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Outlet, NavLink, useParams } from "react-router-dom";
import { thunkGetUserById } from "../../redux/user";
import "./UserProfileLayout.css";

function UserProfileLayout() {
	const [isLoaded, setIsLoaded] = useState(false);
	const dispatch = useDispatch();
	const { userId } = useParams();

	// ! the user profile page immediately show the new username and first initial once the user goes into a different account.
	useEffect(() => {
		const fetchUser = async () => {
			await dispatch(thunkGetUserById(userId));
			setIsLoaded(true);
		};

		if (!isLoaded) {
			fetchUser();
		}
	}, [dispatch, userId, isLoaded]);

	const firstName = useSelector((state) => state.user.firstName);
	const username = useSelector((state) => state.user.username);

	if (!isLoaded) return <h1 style={{ textAlign: "center" }}>Loading...</h1>;

	return (
		<>
			<div
				className="top"
				style={{ diplay: "flex", flexDirection: "column", alignItems: "center" }}>
				<div className="circle">{isLoaded && firstName[0]}</div>
				<div>
					<h1>{username}</h1>
				</div>
			</div>
			<nav>
				<div>
					<NavLink
						className={({ isActive }) => (isActive ? "userNav active" : "userNav inactive")}
						to="stashes">
						Stashes
					</NavLink>
					<NavLink
						className={({ isActive }) => (isActive ? "userNav active" : "userNav inactive")}
						to="posted-images">
						Posted Images
					</NavLink>
				</div>
			</nav>
			<main>
				<Outlet />
			</main>
		</>
	);
}

export default UserProfileLayout;
