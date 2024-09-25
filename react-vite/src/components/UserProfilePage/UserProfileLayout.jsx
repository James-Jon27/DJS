import { useSelector } from "react-redux"
import { Outlet, NavLink } from "react-router-dom";
import "./UserProfileLayout.css"

function UserProfileLayout() {
    const firstInitial = useSelector(state => state.session.user.firstName)[0]

    return (
        <>
            <div className="top">
                <div className="circle">{firstInitial}</div>
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