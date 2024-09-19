const ADD_IMAGE = 'image/ADD'

const addPost = (image) => ({
    type: ADD_IMAGE,
    payload: image
})

export const createPost = (post) => async (dispatch) => {
	const response = await fetch(`/images/new`, {
		method: "POST",
		body: post,
	});

	if (response.ok) {
		const { resPost } = await response.json();
		dispatch(addPost(resPost));
	} else {
		console.log("There was an error making your post!");
	}
};

initialState = {image : null}

export default function imageReducer(state = initialState, action) {
    switch(action.type) {
        case ADD_IMAGE:
            return { ...state, image: action.payload}
    }
}
