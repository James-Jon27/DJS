import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
	return (
		<ul className="nav">
			<div className="left">
				<li>
					<NavLink to="/">Home</NavLink>
				</li>
				<li>Explore</li>
				<li>Create</li>
			</div>
      <div className="search-cont">

      <input
      className="search"
      type="search"
      placeholder="Search"
      />
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
