import { createBrowserRouter } from "react-router-dom";
// import LoginFormPage from '../components/LoginFormPage';
// import SignupFormPage from '../components/SignupFormPage';
import {
	UserProfileLayout,
	UserProfilePostedImage,
	UserProfileStash,
} from "../components/UserProfilePage";
import HomePage from "../components/HomePage";
import ExplorePage from "../components/ExplorePage/ExplorePage";
import UploadImagePage from "../components/UploadImagePage";
import Layout from "./Layout";
import UploadStash from "../components/UploadStash";
import UpdateImage from "../components/UploadImagePage/UpdateImage";
import UpdateStash from "../components/UploadStash/UpdateStash";

export const router = createBrowserRouter([
	{
		element: <Layout />,
		children: [
			{
				path: "/",
				element: <HomePage />,
			},
			{
				path: "explore",
				element: <ExplorePage />,
			},
			{
				path: "user",
				element: <UserProfileLayout />,
				children: [
					{
						path: "posted-images",
						element: <UserProfilePostedImage />,
					},
					{
						path: "stashes",
						element: <UserProfileStash />,
					},
				],
			},
			{
				path: "images/new",
				element: <UploadImagePage />,
			},
			{
				path: "images/:id/edit",
				element: <UpdateImage />,
			},
			{
				path: "stashes/new",
				element: <UploadStash />,
			},
			{
				path: "stashes/:id",
				element: <h1>STASH PAGE COMPONENT COMING SOON</h1>,
			},
			{
				path: "stashes/:id/edit",
				element: <UpdateStash />,
			},
			{
				path: "*",
				element: "Page Not Found",
			},
		],
	},
]);
