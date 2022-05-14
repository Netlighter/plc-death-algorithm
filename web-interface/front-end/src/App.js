import './App.css';
import HeaderStyled from './components/Header/Header';
import { Row, Col } from 'antd';
import { Card } from 'antd';
import { Layout } from 'antd';

const { Footer, Content } = Layout;


function App() {
  return (
    <div className="App">
      <Layout style={{ overflow: 'hidden'}}>
          <HeaderStyled />
        <Content style={{ padding: '50px 50px', minHeight: '80vh'}}>
          <Row gutter={[24, 24]}>
            <Col span={12}>
              <div className="site-card-border-less-wrapper">
                <Card
                  title="Card title"
                  bordered={false}
                >
                  <p>Card content</p>
                  <p>Card content</p>
                  <p>Card content</p>
                </Card>
              </div>
            </Col>
            <Col span={12}>
              <div className="site-card-border-less-wrapper">
                <Card
                  title="Card title"
                  bordered={false}
                >
                  <p>Card content</p>
                  <p>Card content</p>
                  <p>Card content</p>
                </Card>
              </div>
            </Col>
            <Col span={12}>
              <div className="site-card-border-less-wrapper">
                <Card
                  title="Card title"
                  bordered={false}
                >
                  <p>Card content</p>
                  <p>Card content</p>
                  <p>Card content</p>
                </Card>
              </div>
            </Col>
            <Col span={12}>
              <div className="site-card-border-less-wrapper">
                <Card
                  title="Card title"
                  bordered={false}
                >
                  <p>Card content</p>
                  <p>Card content</p>
                  <p>Card content</p>
                </Card>
              </div>
            </Col>
          </Row>
        </Content>
        <Footer>Prominet</Footer>
      </Layout>
    </div>
  );
}

export default App;

