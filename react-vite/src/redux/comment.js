const IMAGE_COMMENTS = "image/comments";
const ADD_COMMENT = `comments/add`;
// 80 comments in this style: comment79 = Comment(user_id=5, image_id=35, comment="So inspiring!") numbered comment80 - comment160
// give me a PYTHON LIST with these variable names without ""

const imageComments = (comments) => {
	return {
		type: IMAGE_COMMENTS,
		payload: comments,
	};
};

const addComment = (comment) => {
	return {
		type: ADD_COMMENT,
		payload: comment,
	};
};

export const getImageComments = (id) => async (dispatch) => {
	const res = await fetch(`/api/images/${id}/comments`);
	const data = await res.json();
	dispatch(imageComments(data));
};

export const postComment = (imageId, comment) => async (dispatch) => {
	const res = await fetch(`/api/images/${imageId}/new_comment`, {
		method: "POST",
		body: comment,
	});
	const data = await res.json();
	dispatch(addComment(data));
    return data;
};

const initialState = {};

function commentReducer(state = initialState, action) {
	switch (action.type) {
		case IMAGE_COMMENTS:
			return action.payload;
		case ADD_COMMENT: {
			const ap = action.payload;
			const newState = { ...state };
			newState[ap.id] = action.payload;
			return newState;
		}
		default:
			return state;
	}
}

export default commentReducer;
