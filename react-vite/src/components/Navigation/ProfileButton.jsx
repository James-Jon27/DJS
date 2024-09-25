import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FaUserLarge } from "react-icons/fa6";
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { NavLink, useNavigate } from "react-router-dom";

function ProfileButton() {
	const nav = useNavigate()
	const dispatch = useDispatch();
	const [showMenu, setShowMenu] = useState(false);
	const user = useSelector((store) => store.session.user);
	const ulRef = useRef();

	const toggleMenu = (e) => {
		e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
		setShowMenu(!showMenu);
	};

	useEffect(() => {
		if (!showMenu) return;

		const closeMenu = (e) => {
			if (ulRef.current && !ulRef.current.contains(e.target)) {
				setShowMenu(false);
			}
		};

		document.addEventListener("click", closeMenu);

		return () => document.removeEventListener("click", closeMenu);
	}, [showMenu]);

	const closeMenu = () => setShowMenu(false);

	const logout = (e) => {
		e.preventDefault();
		dispatch(thunkLogout());
		closeMenu();
		nav("/")
	};

	const faviconStyle = { fontSize: "28px", padding: "0" };

	return (
		<>
			<button onClick={toggleMenu} className="user">
				<FaUserLarge style={faviconStyle} />
			</button>
			{showMenu && (
				<ul className={"profile-dropdown"} ref={ulRef}>
					{user ? (
						<>
							<NavLink to={"/user"}  className="user-page">
								<li>{user.username}</li>
							</NavLink>
							<li>{user.email}</li>
							<li>
								<button onClick={logout}>Log Out</button>
							</li>
						</>
					) : (
						<ul className="hidden">
							<li className="mods">
								<OpenModalMenuItem
									itemText="Log In"
									onItemClick={closeMenu}
									modalComponent={<LoginFormModal />}
								/>
							</li>
							<li className="mods">
								<OpenModalMenuItem
									itemText="Sign Up"
									onItemClick={closeMenu}
									modalComponent={<SignupFormModal />}
								/>
							</li>
						</ul>
					)}
				</ul>
			)}
		</>
	);
}

export default ProfileButton;
