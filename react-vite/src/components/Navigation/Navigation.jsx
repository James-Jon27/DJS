import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
	return (
		<ul className="nav">
			<div className="left">
				<NavLink className="navs" to="/">
					<li>Home</li>
				</NavLink>
				<NavLink className="navs" to="/explore">
					<li>Explore</li>
				</NavLink>
				<NavLink className="navs" to="/">
					<li>Create</li>
				</NavLink>
			</div>
			<div className="search-cont">
				<input className="search" type="search" placeholder="Search" />
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
