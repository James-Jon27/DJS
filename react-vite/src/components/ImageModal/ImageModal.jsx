import { useDispatch, useSelector } from "react-redux";
import { getImageById } from "../../redux/image";
import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import "./ImageModal.css";

export default function ImageModal({ id }) {
	const dispatch = useDispatch();
	const userStashes = useSelector((state) => state.session.user.Stashes);
	const imageSelect = useSelector((state) => state.image);
	const image = imageSelect[id];

    const [checkedStashes, setCheckedStashes] = useState(new Set());

	useEffect(() => {
		dispatch(getImageById(id));
	}, [dispatch, id]);

    useEffect(()=>{
        if (image) {
            const initStashSet = new Set(image.Stashes.map(stash => stash.id))
            setCheckedStashes(initStashSet)
        }
    }, [image])

	const drop = () => {
		document.getElementById("myDropdown").classList.toggle("show");
	};

    const checkbox = (stashId) => {
        const currChecks = new Set(checkedStashes)
        if(currChecks.has(stashId)){
            currChecks.delete(stashId)
        } else {
            currChecks.add(stashId)
        }
        setCheckedStashes(currChecks)
    } 

	if (!image) {
		return <h1>💥</h1>;
	}

	const owner = image.User;
    const comments = image.Comments
    const faves = image.Favorites.length
	console.log(image);

	return (
		<div className="imgPage">
			<div className="imgUser">
				<div className="img-modal">
					<img src={image.url} alt={image.title} />
				</div>
				<div className="userInt">
					<div className="prof">
						<NavLink className="circle" to={`user/${owner.id}`}>
							{owner.firstName[0]}
						</NavLink>
					</div>
					<div className="stashDropdown">
						<div className="dropdown">
							<button className="dropbtn" onClick={drop}>
								Dropdown
							</button>
							<div id="myDropdown" className="dropdown-content">
								{userStashes.map((stash) => {
									return (
										<label key={stash.id}>
                                            <input 
                                                type="checkbox"
                                                checked={checkedStashes.has(stash.id)}
                                                onChange={() => checkbox(stash.id)}
                                            />
                                            {stash.name}
                                        </label>
									);
								})}
							</div>
						</div>
					</div>
					<div className="favorite">
						<button>Favorite</button>
					</div>
				</div>
			</div>
			<span className="imgInfo">
				{image.title && <h1>{image.title}</h1>}
                {image.description && <p>{image.description}</p>}
				<p>Image has {faves} favorites</p>
			</span>
			<span className="comments">
                {comments.map(comment => {
                    return (
                        <div key={comment.id}>
                            <h4>Username</h4>
                            <p>{comment.comment}</p>
                        </div>
                    )
                })}
            </span>
		</div>
	);
}
