const POST_IMAGE = 'images/postImage'
const GET_IMAGES = 'images/getImages'
const GET_ONE_IMAGE = 'images/getImageById'
const DELETE_IMAGE = 'images/delete'
const UPDATE_IMAGE = 'image/update'

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

const deleteImg = (id) => ({
    type: DELETE_IMAGE,
    payload: id
})

const updateImg = (image) => ({
    type: UPDATE_IMAGE,
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

export const deleteImage = (id) => async (dispatch) => {
    await fetch(`/api/images/${id}`, {
        method: "DELETE"
    })
    dispatch(deleteImg(id))
}

export const userImages = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/images`)
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

export const updateImage = (id, update) => async (dispatch) => {
    const res = await fetch(`/api/images/${id}`,{
        method: "PUT",
        body: update
    })
    const data = await res.json();
    dispatch(updateImg(data))
}

export const imageByLabel = (label) => async (dispatch) => {
    const res = await fetch(`/api/images/${label}`)
    const data = res.json()
    dispatch(getImgs(data))
}

function imageReducer(state = {}, action){
    switch(action.type){
        case POST_IMAGE:{
            return { ...state, [action.payload.id]:action.payload }
        }
        case GET_IMAGES:{
            return action.payload
        }
        case GET_ONE_IMAGE:{
            return {...state, [action.payload.id]:action.payload}
        }
        case DELETE_IMAGE:{
            const newState = {...state}
            delete newState[action.payload]
            return newState
        }
        case UPDATE_IMAGE:{
            return {...state, [action.payload.id]:action.payload}
        }
        default:
            return state
    }
}

export default imageReducer