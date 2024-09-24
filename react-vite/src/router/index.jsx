import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import { UserProfileLayout, UserProfilePostedImage, UserProfileStash } from '../components/UserProfilePage'
import UploadImagePage from '../components/UploadImagePage'
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <h1>Welcome!</h1>,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "user",
        element: <UserProfileLayout />,
        children: [
          {
            path: "posted-images",
            element: <UserProfilePostedImage />
          },
          {
            path: "stashes",
            element: <UserProfileStash />
          }
        ]
      },
      {
        path: "/images/new",
        element: <UploadImagePage />
      }
      
    ],
  },
]);