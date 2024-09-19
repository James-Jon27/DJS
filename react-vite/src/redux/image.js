const POST_IMAGE = 'images/postImage'

const addPost = (image) => ({
    type: POST_IMAGE,
    payload: image
})


export const createImage = (post) => async (dispatch) => {
    const response = await fetch(`/api/images/new`, {
      method: "POST",
      body: post
    });
  
    if (response.ok) {
        const data = await response.json();
        console.log(data);
        dispatch(addPost(data));
    } else {
        console.log("There was an error making your post!")
    }
};


function imageReducer(state = {}, action){
    switch(action.type){
        case POST_IMAGE:{
            return { ...state, [action.payload.id]:action.payload }
        }
        default:
            return state
    }
}

export default imageReducer