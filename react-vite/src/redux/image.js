const POST_IMAGE = 'images/postImage'
const GET_IMAGES = 'images/getImages'

const addPost = (image) => ({
    type: POST_IMAGE,
    payload: image
})

const getImgs = (images) => ({
    type: GET_IMAGES,
    payload: images
})


export const getImages = () => async (dispatch) => {
    const res = await fetch(`/api/images`)
    const data = await res.json();
    dispatch(getImgs(data))
}

export const createImage = (post) => async (dispatch) => {
    const res = await fetch(`/api/images/new`, {
      method: "POST",
      body: post
    });
  
    if (res.ok) {
        console.log(res)
        const data = await res.json();
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
        case GET_IMAGES:{
            return {...action.payload.images}
        }
        default:
            return state
    }
}

export default imageReducer