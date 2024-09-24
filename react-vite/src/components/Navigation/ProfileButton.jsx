import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FaUserLarge } from "react-icons/fa6";
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";

function ProfileButton() {
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
  };

  const faviconStyle = {fontSize: "28px", padding: "0"};

  return (
		<>
			<button onClick={toggleMenu} className="user">
				<FaUserLarge style={faviconStyle}/>
			</button>
			{showMenu && (
				<ul className={"profile-dropdown"} ref={ulRef}>
					{user ? (
						<>
							<li>{user.username}</li>
							<li>{user.email}</li>
							<li>
								<button onClick={logout}>Log Out</button>
							</li>
						</>
					) : (
						<ul
							style={{
								alignItems: "center",
								listStyle: "none",
								paddingLeft: "10px",
								paddingRight: "70px",
							}}>
							<OpenModalMenuItem
								itemText="Log In"
								onItemClick={closeMenu}
								modalComponent={<LoginFormModal />}
							/>
							<OpenModalMenuItem
								itemText="Sign Up"
								onItemClick={closeMenu}
								modalComponent={<SignupFormModal />}
							/>
						</ul>
					)}
				</ul>
			)}
		</>
	);
}

export default ProfileButton;
