import { NavLink } from "react-router-dom"
import "./UserProfileLayout.css"

function UserProfileLayout() {
    return (
        <>
            <div className="top">
                <div className="circle">This is your User Profile Page!</div>
            </div>
            <nav>
                <div>
                    <NavLink className="userNav">Stashes</NavLink>
                    <NavLink className="userNav">Posted Images</NavLink>
                </div>
            </nav>
        </>
    )
}

export default UserProfileLayout