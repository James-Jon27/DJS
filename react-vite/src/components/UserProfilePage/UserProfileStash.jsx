import { useSelector } from 'react-redux';
import './UserProfileStash.css'

function UserProfileStash() {
    const userStashes = useSelector(state => state.session.user.Stashes);

    return (
        <div className='Stashes'>
            <div className='Favorite'>
                Favorites
            </div>
            {userStashes.map(stash => {
                return (
                    <div key={stash.id} className='Stash'>
                        {stash.name}
                    </div>
                )
            })}
        </div>
    )
}

export default UserProfileStash