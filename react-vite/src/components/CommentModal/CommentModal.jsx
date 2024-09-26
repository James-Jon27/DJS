import { useDispatch } from "react-redux"
import { useModal } from "../../context/Modal"
import { useState } from "react";
import { postComment } from "../../redux/comment";

export default function CommentModal({image}){
    const dispatch = useDispatch()
    const {closeModal} = useModal();
    const [comment, setComment] = useState("")

    const handelSubmit = async (e) => {
        e.preventDefault()

        const res = await dispatch(postComment(image, comment))
        if(res) {
            closeModal()
        }
    }

    const disabled = () => (comment.length < 10 ? true : false);

    return (
        <div className="commentModal">
            <h1>What do you want to say?</h1>
            <form onSubmit={handelSubmit}>
                <textarea placeholder="Leave your comment here..." value={comment} onChange={(e) => {setComment(e.target.value)}}/>
                <button className="commentButt" type="submit" disabled={disabled()}>Submit Comment</button> 
            </form>
        </div>
    )
}