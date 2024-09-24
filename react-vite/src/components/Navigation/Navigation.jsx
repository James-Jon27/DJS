import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <ul className="nav">
      <li>
        <NavLink to="/">Home</NavLink>
      </li>
      <li>
        Explore
      </li>
      <li>
        Create
      </li>

      <li>
        <ProfileButton />
      </li>
    </ul>
  );
}

export default Navigation;
