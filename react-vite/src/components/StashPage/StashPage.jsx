import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams, useNavigate } from 'react-router-dom'
import './StashPage.css'
import { getStashById } from '../../redux/stash'

function StashPage() {
    const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340))
    useEffect(() => {
        function handleColNum() {
            setColNum(parseInt((window.innerWidth - 40) / 340))
        }

        window.addEventListener('resize', handleColNum)

        return () => window.removeEventListener('resize', handleColNum)
    }, [])

    const { id: stashId } = useParams()
    const dispatch = useDispatch()
    const [isLoaded, setIsLoaded] = useState(false)
    useEffect(() => {
        dispatch(getStashById(stashId)).then(() => setIsLoaded(true))
    }, [dispatch, stashId])
    const stash = useSelector(state => state.stash)

    const navigate = useNavigate()

    return (
        isLoaded && 
            (
                <div className='stashContainer'>  
                    <div className='titleUser'>
                        <h1>{stash.name}</h1>
                        <p>- by {stash.User.username}</p>
                    </div>
                    <p id="description">{stash.description}</p>
                    {stash.Images.length
                        ? 
                            (
                                <div className='grid' style={{"--colNum": colNum}}>
                                    {stash.Images.map(image => {
                                    return (
                                        <img src={image.url} key={image.id} />
                                    )
                                    })}
                                </div>
                            )
                        :
                            (
                                <div className='emptyStashBox'>
                                    <h1>No Images Stashed</h1>
                                    <button onClick={() => navigate(`/explore`)}>Go stash some!</button>
                                </div>
                            )
                    }
                </div>
            )
    )
}

export default StashPage