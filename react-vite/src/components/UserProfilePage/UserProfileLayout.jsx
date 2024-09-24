import { Outlet } from "react-router-dom";
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
                    <NavLink className={({isActive}) => isActive ? 'userNav active' : 'userNav inactive' } to="stashes">Stashes</NavLink>
                    <NavLink className={({isActive}) => isActive ? 'userNav active' : 'userNav inactive'} to="posted-images">Posted Images</NavLink>
                </div>
            </nav>
            <main>
                <Outlet />
            </main>
        </>
    )
}

export default UserProfileLayout