const IMAGE_COMMENTS = 'image/comments'

const imageComments = (comments) => {
    return {
        type: IMAGE_COMMENTS,
        payload: comments
    }
}

export const getImageComments = (id) => async (dispatch) => {
    const res = await fetch(`/api/images/${id}/comments`)
    const data = await res.json();
    dispatch(imageComments(data))

} 

function commentReducer(state = {}, action){
    switch(action.type){
        case IMAGE_COMMENTS:
            return action.payload
        default:
            return state
    }
}

export default commentReducer