import { NavLink, useNavigate } from "react-router-dom";
import { useEffect, useRef, useState } from "react";
import { FaSearch } from "react-icons/fa";
import { useDispatch } from "react-redux";
import ProfileButton from "./ProfileButton";
import { getSearchLabel } from "../../redux/searchLabel";
import "./Navigation.css";
import { useSelector } from "react-redux";

function Navigation() {
	const ulRef = useRef();
	const [searchLabel, setSearchLabel] = useState("");
	const navigate = useNavigate()
	const dispatch = useDispatch()
	const [showMenu, setShowMenu] = useState(false);
	const sessionUser = useSelector((state) => state.session.user);

	const toggleMenu = (e) => {
		e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
		setShowMenu(!showMenu);
	};
	const closeMenu = () => setShowMenu(false);

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
	console.log(searchLabel)

	return (
		<ul className="nav">
			<div className="left">
				<NavLink className="navs" to="/">
					<li>Home</li>
				</NavLink>
				<NavLink className="navs" to="/explore" onClick={() => dispatch(getSearchLabel(""))}>
					<li>Explore</li>
				</NavLink>
				{/* TODO: MAKE DROPDOWN THAT SAYS STASH OR IMG, ONLY VISIBLE TO A LOGGED IN USER */}
				{sessionUser && (
					<>
						<li style={{cursor:"pointer"}} onClick={toggleMenu}>Create</li>
						{showMenu && (
							<ul className={"profile-dropdown-create"} ref={ulRef}>
								<NavLink className="navs-create" to="/stashes/new" onClick={closeMenu}>
									<li>Stash</li>
								</NavLink>
								<NavLink className="navs-create" to="/images/new" onClick={closeMenu}>
									<li>Image</li>
								</NavLink>
							</ul>
						)}
					</>
				)}
			</div>
			<div className="search-cont">
				<input
					className="search"
					type="search"
					placeholder="Search for images by label"
					value={searchLabel}
					onChange={(e) => setSearchLabel(e.target.value)}
				/>
				<button 
					onClick={() => {
						dispatch(getSearchLabel(searchLabel))
						navigate(`/explore`)
					}}
					disabled={!searchLabel.length}
				>
					<FaSearch />
				</button>
			</div>
			<div>
				<li className="right">
					<ProfileButton />
				</li>
			</div>
		</ul>
	);
}

export default Navigation;
