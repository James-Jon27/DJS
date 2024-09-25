import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getImages } from '../../redux/image'
import './ExplorePage.css'

function ExplorePage() {
    const [colNum, setColNum] = useState(parseInt((window.innerWidth - 40) / 340))
    useEffect(() => {
        function handleColNum() {
            setColNum(parseInt((window.innerWidth - 40) / 340))
        }

        window.addEventListener('resize', handleColNum)

        return () => window.removeEventListener('resize', handleColNum)
    }, [])

    const dispatch = useDispatch()
    const [isLoaded, setIsLoaded] = useState(false)
    useEffect(() => {
        dispatch(getImages()).then(() => setIsLoaded(true));
    }, [dispatch])
    const images = Object.values(useSelector(state => state.image))

    return (
        <div className='grid' style={{"--colNum": colNum}}>
            {isLoaded && images.map(image => {
                return (
                    <img src={image.url} key={image.id} />
                )
            })}
        </div>
    )
}

export default ExplorePage