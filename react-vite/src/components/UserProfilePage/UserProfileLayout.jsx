import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { Outlet, NavLink, useParams } from "react-router-dom";
import { thunkGetUserById } from '../../redux/user';
import "./UserProfileLayout.css"

function UserProfileLayout() {
    const [isLoaded, setIsLoaded] = useState(false)
    const dispatch = useDispatch()

    const { userId } = useParams()
    useEffect(() => {
        dispatch(thunkGetUserById(userId)).then(() => setIsLoaded(true))
    }, [dispatch, userId])

    const firstName = useSelector(state => state.user.firstName)

    return (
        <>
            <div className="top">
                <div className="circle">{isLoaded && firstName[0]}</div>
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