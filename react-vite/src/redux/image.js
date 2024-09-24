const POST_IMAGE = 'images/postImage'
const GET_IMAGES = 'images/getImages'
const GET_ONE_IMAGE = 'images/getImageById'

const addPost = (image) => ({
    type: POST_IMAGE,
    payload: image
})

const getImgs = (images) => ({
    type: GET_IMAGES,
    payload: images
})

const getOneImg = (image) => ({
    type: GET_ONE_IMAGE,
    payload: image
})


export const getImages = () => async (dispatch) => {
    const res = await fetch(`/api/images`)
    const data = await res.json();
    dispatch(getImgs(data))
}

export const getImageById = (id) => async (dispatch) => {
    const res = await fetch(`/api/images/${id}`)
    const data = await res.json();
    dispatch(getOneImg(data))
}

export const createImage = (post) => async (dispatch) => {
    const res = await fetch(`/api/images/new`, {
      method: "POST",
      body: post
    });
  
    if (res.ok) {
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
        case GET_ONE_IMAGE:{
            return {[action.payload.id]:action.payload}
        }
        default:
            return state
    }
}

export default imageReducer