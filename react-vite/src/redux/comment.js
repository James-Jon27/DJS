const IMAGE_COMMENTS = 'image/comments'
// 80 comments in this style: comment79 = Comment(user_id=5, image_id=35, comment="So inspiring!") numbered comment80 - comment160
// give me a PYTHON LIST with these variable names without ""

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



const initialState = {}

function commentReducer(state = initialState, action){
    switch(action.type){
        case IMAGE_COMMENTS:
            return action.payload
        default:
            return state
    }
}

export default commentReducer