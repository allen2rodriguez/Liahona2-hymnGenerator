import * as React from "react";
import Container from "@cloudscape-design/components/container";
import Header from "@cloudscape-design/components/header";
import Button from "@cloudscape-design/components/button";
import Alert from "@cloudscape-design/components/alert";


export default function Hymns() {
    const [visible, setVisible] = React.useState(true);

    const hymnClick = () => {
        setTimeout(() => {
            alert("ERROR 200: Could not find the server to check for hymns \nPlease don't press the button again!!!!!!!!!!!!!! >:(")
        }, 1250);
        
    }
    return (
        <Container
            header={
            <Header
                variant="h2"
                description=
                    {visible && (
                    <Alert type="info" dismissible onDismiss={() => setVisible(false)}>
                        Esta función aún no está implementada, por favor no presione este botón.                    
                    </Alert> 
                )}
            >
                Hymn Suggestions
            </Header>
            }
        >
            <Button variant="primary" onClick={hymnClick}>Submit Suggestion</Button>
        </Container>
    );
}
