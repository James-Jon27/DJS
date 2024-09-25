import { useParams } from 'react-router-dom'
import './StashPage.css'

function StashPage() {
    const { id: stashId } = useParams()

    return (
        <h1>Welcome to the Stash Id {stashId}!</h1>
    )
}

export default StashPage